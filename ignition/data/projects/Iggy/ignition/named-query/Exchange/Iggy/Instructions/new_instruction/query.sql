INSERT INTO instructions (name, description, content)
VALUES (:name, :description, :content)
RETURNING id;