SELECT *
FROM
    ignition_chat_history
WHERE
    username = :username
ORDER BY
    created_at DESC;