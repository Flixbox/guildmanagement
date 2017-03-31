INSERT INTO `transaction_history` (
    `user_id`,
    `value`,
    `message`,
    `iban_from`,
    `iban_to`,
    `created_at`,
    `updated_at`
    )

VALUES (
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
);