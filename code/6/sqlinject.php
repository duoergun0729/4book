<?php
      $conn=@mysql_connect("localhost",'root','')or die("NO");;
      mysql_select_db("injection",$conn) or die("NO");
      $name=$_POST['username'];
      $pwd=$_POST['password'];
      $sql="select * from users where username='$name' andpassword='$pwd'";
      $query=mysql_query($sql);
      $arr=mysql_fetch_array($query);
      if(is_array($arr)){
             echo "OK";
       }else{
             echo "NO";
       }
?>

