# uzpos-back

- Server configuration for microservices
 - [Server configuration for nginx](#Server-configuration-for-nginx)

# Server configuration for nginx
    .
    ├── etc                   
        |── nginx/
            ├── api_conf.d/ 
                ├── delivery_api.conf 
            ├── api_backends.conf
            ├── api_gateway.conf 
            ├── api_json_errors.conf
            ├── conf.d/
            ├── api_keys.conf/
            └── nginx.conf


## delivery_api.conf
    
    location /api {
        # Policy configuration here (authentication, rate limiting, logging, more...)
        #
        # access_log /var/log/nginx/delivery_api.log main;

        location /api/delivery/static {
            autoindex on;    
            alias "/Users/user/Documents/shoh projects/uzposback/uzpos/static";
        }
        location /api/delivery {
                proxy_pass http://delivery;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;        
        }

        return 404; # Catch-all
    }
    
## api_backends.conf
    
    upstream delivery {
        zone delivery_service 128k;
        server 127.0.0.1:8001;    
    }
    
## api_gateway.conf 
    
    include api_backends.conf;
    include api_keys.conf;

    server {
        # access_log /var/log/nginx/api_access.log main; # Each API may also log to a separate file
        listen 80;
        server_name localhost;

        # API definitions, one per file
        include api_conf.d/*.conf;

        # Error responses
        error_page 400 = @400;
        location @400 { return 400 '{"status":400,"message":"Bad request"}\n'; }

        error_page 401 = @401;
        location @401 { return 401 '{"status":401,"message":"Unauthorized"}\n'; }

        error_page 403 = @403;
        location @403 { return 403 '{"status":403,"message":"Forbidden"}\n'; }

        error_page 404 = @404;
        location @404 { return 404 '{"status":404,"message":"Resource not found"}\n'; }
        # Error responses
        proxy_intercept_errors on;     # Do not send backend errors to the client
        # include api_json_errors.conf;  # API client friendly JSON error responses
        default_type application/json; # If no content-type then assume JSON
    }
    
## nginx.conf
    
    http {
        include /opt/homebrew/etc/nginx/api_gateway.conf;
        include       mime.types;
        default_type  application/octet-stream;

        sendfile        on;

        keepalive_timeout  65;

        server {
            listen       8080;
            server_name  localhost;

            #charset koi8-r;

            #access_log  logs/host.access.log  main;

            location / {
                root   html;
                index  index.html index.htm;
            }
        }


        include servers/*;
    }

## api_keys.conf
    map $http_apikey $api_client_name {
        default "";

        "7B5zIqmRGXmrJTFmKa99vcit" "client_one";
        "QzVV6y1EmQFbbxOfRCwyJs35" "client_two";
        "mGcjH8Fv6U9y3BVF9H3Ypb9T" "client_six";
    }