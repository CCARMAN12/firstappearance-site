-- Opens the admin dashboard, starting the server first if it is not up.
--
-- A shortcut that lands on a dead port is worse than no shortcut: it teaches
-- you not to trust the icon. So this probes, starts casewire serve if nothing
-- answers, waits for it, and only then opens the page.
--
-- Absolute paths throughout: `do shell script` runs with a minimal PATH that
-- does not include Homebrew, so a bare `uv` is not found.
on run
	set base to "http://127.0.0.1:8000"
	set probe to "/usr/bin/curl -s -o /dev/null -m 2 " & quoted form of (base & "/login")
	set alreadyUp to true
	try
		do shell script probe
	on error
		set alreadyUp to false
	end try

	if not alreadyUp then
		do shell script "cd /Users/craigcarman/Developer/casewire && " & ¬
			"/usr/bin/nohup /opt/homebrew/bin/uv run casewire serve " & ¬
			"> /tmp/casewire-serve.log 2>&1 &"
		set ready to false
		repeat 40 times
			delay 0.5
			try
				do shell script probe
				set ready to true
				exit repeat
			end try
		end repeat
		if not ready then
			display dialog "The admin server did not come up within 20 seconds." & ¬
				return & return & "Check /tmp/casewire-serve.log" ¬
				buttons {"OK"} default button "OK" with icon caution
			return
		end if
	end if

	open location (base & "/admin")
end run
