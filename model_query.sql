select 
  users.username users_username,
  users.document_id users_document_id,
  users.email users_email,
  users.createdAt_ts users_createdAt_ts,
  users.modifiedAt_ts users_modifiedAt_ts,
  items.document_id items_doc_id,
  items.UserId items_user_id,
  items.ItemName items_itemname,
  items.createdAt_ts items_createdAt_ts,
  items.modifiedAt_ts items_modifiedAt_ts
from 
`roofstack_case.Users` as users 
left join `roofstack_case.Items` as items 
on users.document_id = items.UserId