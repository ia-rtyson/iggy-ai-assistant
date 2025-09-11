SELECT id, name, description,
ts_rank_cd(
        to_tsvector('english', content),
        plainto_tsquery('english', :query)
    ) AS rank
FROM instructions
WHERE to_tsvector('english', content) @@ plainto_tsquery('english', :query)
ORDER BY rank DESC;