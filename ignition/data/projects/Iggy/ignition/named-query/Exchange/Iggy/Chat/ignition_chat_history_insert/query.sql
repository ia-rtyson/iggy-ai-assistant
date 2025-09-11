INSERT INTO ignition_chat_history (username, description)
VALUES (:username, :description)
RETURNING id;