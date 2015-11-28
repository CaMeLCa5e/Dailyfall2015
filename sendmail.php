$msg = "a message";
$subject = "a subject";
mail($_POST['email1'], $subject,$msg,'From: ' . $_POST['sendername'] . "\n\r" );
mail($_POST['email2'], $subject,$msg,'From: ' . $_POST['sendername'] . "\n\r" );
mail($_POST['email3'], $subject,$msg,'From: ' . $_POST['sendername'] . "\n\r" );
mail($_POST['email4'], $subject,$msg,'From: ' . $_POST['sendername'] . "\n\r" );
mail($_POST['email5'], $subject,$msg,'From: ' . $_POST['sendername'] . "\n\r" );