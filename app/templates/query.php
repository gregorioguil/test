<?php
// Connect to Mongo and set DB and Collection
$mongo = new MongoClient();
$db = $mongo->test_database;
$collection = $db->test_collection;
// Return a cursor of data from MongoDB
$cursor = $collection->find();
$i=0;
foreach ($cursor as $value) {
   $return[$i] = array (
      'time' => $value['time'],
      'id' => $value['id']
   );
   $i++;
}
echo json_encode($return);
?>
