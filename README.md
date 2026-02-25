# niyara

From → your Gmail (MAIL_USERNAME in .env)
To → recipient_email field from the form, hardcoded on the frontend as hello@niyaratissues.com
The customer's email (form_data.email) appears inside the HTML body, not as the actual sender — this is intentional since you're relaying through Gmail