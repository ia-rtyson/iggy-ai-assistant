INSERT INTO instructions (name, description, content)
VALUES (:name, :description, :content)
ON CONFLICT (name)
DO UPDATE SET
    description = EXCLUDED.description,
    content     = EXCLUDED.content
RETURNING id;