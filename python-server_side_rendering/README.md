# Python Server-Side Rendering

Server-side rendering (SSR) is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data. This project explores implementing SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.

## Learning Objectives

- Understand server-side rendering concepts and how it differs from client-side rendering
- Learn the benefits of using server-side rendering in web development
- Implement SSR in Python using the Flask framework
- Utilize the Jinja templating engine to dynamically generate HTML pages
- Read and display data from various sources (JSON, CSV, SQLite)
- Handle dynamic content and user inputs in web applications

## Project Tasks

### 0. Creating a Simple Templating Program

- Create a Python function `generate_invitations` that generates personalized invitation files from a template
- Handle placeholders for `name`, `event_title`, `event_date`, and `event_location`
- Implement error handling for various cases (empty template, missing data, invalid inputs)
- Write output files named sequentially (e.g., `output_1.txt`, `output_2.txt`, etc.)

### 1. Creating a Basic HTML Template in Flask

- Set up a Flask application to serve web pages using Jinja templates
- Create an `index.html` template with basic HTML elements
- Implement reusable components with `header.html` and `footer.html`
- Create additional pages (`about.html`, `contact.html`) that include the shared components
- Define Flask routes for each page (`/about`, `/contact`)

### 2. Creating a Dynamic Template with Loops and Conditions in Flask

- Create a template that uses Jinja's loop and conditional constructs
- Read items from a JSON file and display them dynamically
- Implement a conditional statement to display a message when the list is empty
- Create a new route (`/items`) to render the dynamic template

### 3. Displaying Data from JSON or CSV Files in Flask

- Build a feature to read and display product data from JSON and CSV files
- Create a single template that works with multiple data sources
- Implement query parameters to determine the data source and filtering criteria
- Handle edge cases like invalid source parameters or missing products

### 4. Extending Dynamic Data Display to Include SQLite in Flask

- Add functionality to fetch and display data from a SQLite database
- Create and populate a `Products` table in a SQLite database
- Extend the existing template to handle data from the database
- Implement error handling for database-related issues

## Resources

- [MDN Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side)
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)