import webapp2

html ="""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="my.css" />
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js">
        </script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js">
        </script>
        <script src="my.js">
        </script>
    </head>
    <body>
        <!-- Home -->
        <div data-role="page" id="page1">
			<form action = "/chooseform">
				<input name=chooseform>
					<div data-role="content" style="padding: 15px">
						<div data-role="fieldcontain">
							<fieldset data-role="controlgroup" data-type="vertical" data-mini="true">
								<legend>
									Choices:
								</legend>
								<input name="checkbox1" id="checkbox1" type="checkbox" />
								<label for="checkbox1">
									A
								</label>
								<input name="checkbox2" id="checkbox2" type="checkbox" />
								<label for="checkbox2">
									B
								</label>
								<input name="checkbox3" id="checkbox3" type="checkbox" />
								<label for="checkbox3">
									C
								</label>
							</fieldset>
						</div>
					</div>
				<input type="submit" value="submit">
			</form>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
class ChooseForm(webapp2.RequestHandler):
	def get(self):
		

app = webapp2.WSGIApplication([('/', MainHandler),(/chooseform,ChooseForm)],
                              debug=True)
