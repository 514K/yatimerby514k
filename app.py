#!/usr/bin/python3

print("""Content-Type: text/html; charset=utf-8 \n\n
	<head>
	  <script type="text/javascript"> 
	    "use strict";
	    function userTime() {
		   let time=new Date();
		   document.getElementById('userTime').innerHTML =
			(time.getHours() < 10 ? "0" + time.getHours() : time.getHours())
			+ ":" +
			(time.getMinutes() < 10 ? "0" + time.getMinutes() : time.getMinutes())
			+ ":" +
			(time.getSeconds() < 10 ? "0" + time.getSeconds() : time.getSeconds());

		   setTimeout("userTime()",1000);
	    }
	  </script>
	</head>
	<body onload="userTime()"> <p id="userTime"> </p> </body>""")
