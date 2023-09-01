with main as
(select 
  data,
  document_id,
  json_extract_scalar(`data`, "$.username") username,
  json_extract_scalar(`data`, "$.email") email,
  cast(json_extract_scalar(`data`, "$.createdAt._seconds")as int64) createdAt,
  cast(json_extract_scalar(`data`, "$.modifiedAt._seconds")as int64) modifiedAt
from `firestore_Items.Users_raw_latest`)
select 
  document_id,
  main.username,
  main.email,
  timestamp_seconds(main.createdAt) createdAt_ts,
  timestamp_seconds(main.modifiedAt) modifiedAt_ts
from main