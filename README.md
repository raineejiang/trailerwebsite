# Movie Trailer Website
## Project Summary
This is the first project for the Full-stack Nanodegree Program. This project is to create a movie trailer website including box art imagery and a movie trailer URL. The data will be served as a webpage allowing visitors to review their movies and watch the trailers.
## Installation
* Make sure to download all of the files in this repository and save the files in the same local folder. The files include, fresh_tomatoes.html, fresh_tomatoes.py, media.py, entertainment_center.py, README.md. 
* Open entertainment_center.py through IDLE and then run the module. The trailer web page should pop up in the browser properly.
## Content
* media.py: The movie class is defined in this python file.
* entertainment_center.py: Six instances of the movie class are created in this python file to provide data for the trailer web page.
* fresh_tomatoes.py: A key function, `open_moview_page()` is used in this module to take in a list of movies and generate an HTML file including this content, producing a website to showcase the movies. 
```def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
```
* fresh_tomatoes.html: This HTML file contains HTML code for the trailer website appearance.
