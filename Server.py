import cherrypy


class SimpleWebsite:
    @cherrypy.expose
    def index(self):
        return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Enter a Topic, Get a Video Explanation</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Titillium Web', sans-serif;
                background-color: #f0f2f5;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                height: 100vh;
            }

            h1 {
                text-align: center;
                margin-top: 100px;
                margin-bottom: 40px;
                font-size: 52px;
                color: #4CAF50;
                font-weight: bold;
            }

            .container {
                width: 600px;
                background-color: #fff;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

            label {
                font-weight: bold;
                display: block;
                margin-bottom: 8px;
            }

            input[type="text"] {
                width: 100%;
                padding: 8px;
                margin-bottom: 24px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            select {
                width: 100%;
                padding: 8px;
                margin-bottom: 24px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            input[type="submit"] {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 12px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
                width: 100%;
            }
        </style>
    </head>
    <body>
    <h1>Enter a Topic, Get a Video Explanation</h1>
    <div class="container">
        <form action="submit" method="post">
            <label for="topic">Topic:</label>
            <input type="text" id="topic" name="topic" required><br>
            <label for="name">Name:</label>
            <select id="name" name="name">
                <option value="Ice Spice">Ice Spice</option>
                <option value="Donald Trump">Donald Trump</option>
                <option value="Pop Smoke">Pop Smoke</option>
                <option value="David Goggins">David Goggins</option>
                <option value="Queen Elizabeth">Queen Elizabeth</option>
                <option value="Barack Obama">Barack Obama</option>
                <option value="Lebron James">Lebron James</option>
                <option value="Joe Biden">Joe Biden</option>
                <option value="Joe Rogan">Joe Rogan</option>
                <option value="Ben Shapiro">Ben Shapiro</option>
            </select><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
    '''

    @cherrypy.expose
    def submit(self, topic=None, name=None):
        if topic and name:
            cherrypy.session['topic'] = topic
            cherrypy.session['name'] = name
            return f"Received topic: {topic}, selected name: {name}"
        else:
            return "Error: Missing topic or name"


if __name__ == "__main__":
    cherrypy.config.update({'tools.sessions.on': True})
    cherrypy.quickstart(SimpleWebsite())


