with main as
(select 
  data,
  document_id,
  json_extract_scalar(`data`, "$.itemName") ItemName,
  json_extract_scalar(`data`, "$.userId") UserId,
  cast(json_extract_scalar(`data`, "$.createdAt._seconds")as int64) createdAt,
  cast(json_extract_scalar(`data`, "$.modifiedAt._seconds")as int64) modifiedAt
from `firestore_Items.Items_raw_latest`)
select 
  document_id,
  main.ItemName,
  main.UserId,
  timestamp_seconds(main.createdAt) createdAt_ts,
  timestamp_seconds(main.modifiedAt) modifiedAt_ts
from main