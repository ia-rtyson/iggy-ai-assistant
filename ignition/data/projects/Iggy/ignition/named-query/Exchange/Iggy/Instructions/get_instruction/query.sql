SELECT
    id,
    name,
    description,
    content,
    created_at,
    updated_at
FROM instructions
WHERE id = :id;