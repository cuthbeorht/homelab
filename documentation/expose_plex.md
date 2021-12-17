# Exposing Plex

## Copy Config

Swag provides pre-configured Nginx conf files for reverse proxies (https://github.com/linuxserver/reverse-proxy-confs). I took the one for plex as a subfolder and, 
since plex is running in host network mode, just pointed my browser to my domain/plex. 

However, I thought against leaving it public since I don't want to expose my music library... yet.

## Next Steps

- Figure out how to lock down Plex so only I can access it. Until then I am leaving it running in my network but not exposed to the web.