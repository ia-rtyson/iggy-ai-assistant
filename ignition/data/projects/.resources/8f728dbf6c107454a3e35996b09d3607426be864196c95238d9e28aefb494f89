SELECT
    h.interaction_number,
	h.timestamp as "timestamp",
	h.session_id as session_id,
	'message' as event_type,
    CASE
        WHEN h.message->>'type' = 'human' THEN 0          -- human
        ELSE 2                                           -- AI / bot
    END                               AS sort_group,
    h.message->>'type'                AS message_type,        -- e.g. 'human', 'bot', …
    h.message::text             AS content,
    h.id                              AS item_id
--    'chat_history'                    AS source_table
--    NULL                              AS artifact_id,        -- no artifact
--    NULL                              AS artifact_type      -- no artifact
FROM public.n8n_chat_history h
WHERE h.session_id = :chat_id
  AND NOT h.hide

UNION ALL
SELECT
    a.interaction_number,
	a.timestamp AS "timestamp",
	a.ignition_chat_history_chat_id as session_id,
	at.name AS event_type,
    1                                 AS sort_group,          -- artifact  → 2
    'artifact'                        AS message_type,
    a.data                            AS content,
    a.id                              AS item_id
--    'artifacts'                      AS source_table
--    a.id                              AS artifact_id,
--    a.artifact_type_id                AS artifact_type
FROM public.ignition_chat_artifacts a
INNER JOIN
    artifact_type AS at ON a.artifact_type_id = at.id
WHERE a.ignition_chat_history_chat_id = :chat_id

ORDER BY
    interaction_number,
    sort_group,                 -- 0 = human, 1 = artifact, 2 = others
    session_id;