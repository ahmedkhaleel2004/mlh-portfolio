server {
    listen 80;
    server_name ahmed-mlh.duckdns.org;

    if ($host = ahmed-mlh.duckdns.org) {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name ahmed-mlh.duckdns.org;

    location / {
        proxy_pass http://myportfolio:5000/;
    }

    # Load the certificate files.
    ssl_certificate /etc/letsencrypt/live/myportfolio/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myportfolio/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/myportfolio/chain.pem;
}
