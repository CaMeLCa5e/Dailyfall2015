<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
 
<html xmlns='http://www.w3.org/1999/xhtml'>
   <head >
      <meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>
      <title >Form Page: sampleform</title>
   </head>
<body>
<h1>Sample form page</h1>
 
<form id='sampleform' method='post' action='' >
   <p>
   Name: <input type='text' name='Name' />
   </p>
   <p>
   Email: <input type='text' name='Email' />
   </p>
   <p>
   <input type='submit' name='Submit' value='Submit' />
   </p>
</form>
 
</body>
</html>


<?php 
$action=$_REQUEST['action']; 
if ($action=="")    /* display the contact form */ 
    { 
    ?> 
    <form  action="" method="POST" enctype="multipart/form-data"> 
    <input type="hidden" name="action" value="submit"> 
    First:<br> 
    <input name="name" type="text" value="" size="30"/><br> 
    Email:<br> 
    <input name="email" type="text" value="" size="30"/><br> 
    Message:<br> 
    <textarea name="message" rows="7" cols="30"></textarea><br> 
    <input type="submit" value="Send email"/> 
    </form> 
    <?php 
    }  
else                /* send the submitted data */ 
    { 
    $name=$_REQUEST['name']; 
    $email=$_REQUEST['email']; 
    $message=$_REQUEST['message']; 
    if (($name=="")||($email=="")||($message=="")) 
        { 
        echo "All fields are required, please fill <a href=\"\">the form</a> again."; 
        } 
    else{         
        $from="From: $name<$email>\r\nReturn-path: $email"; 
        $subject="Message sent using your contact form"; 
        mail("youremail@yoursite.com", $subject, $message, $from); 
        echo "Email sent!"; 
        } 
    }   
?> 