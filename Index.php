<html>
<head>

</head>
<body>
  <h1>
  Welcome to the the online image converter 
  the project is currently in the earliest of early stages 

  </h1>
    <script>
    function myFunction() {
    var x = document.createElement("INPUT");
    x.setAttribute("type", "file");
    document.body.appendChild(x);}
    </script>
   
    <!-- THIS IS THE GO ELEMENT FOR THE PYTON CONVERSION SCRIPT DO NOT-->
    <div id="button"><button onclick="myFunction();">Convert</button></div>

  <?php
   function getimg{
    echo $_SERVER['PHP_SELF'];
    echo "<br>";
    echo $_SERVER['SERVER_NAME'];
    echo "<br>";
    echo $_SERVER['HTTP_HOST'];
    echo "<br>";
    echo $_SERVER['HTTP_REFERER'];
    echo "<br>";
    echo $_SERVER['HTTP_USER_AGENT'];
    echo "<br>";
   }
?>
</body>
</html>
