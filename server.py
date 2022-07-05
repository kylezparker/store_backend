from flask import Flask

app= Flask ('server')
# print("hello from server")




@app.get("/")
def home():
    return "hello from server"

@app.get("/test")
def test():
    return "test"



@app.get("/about")
def about():
    return "this is the bookstore"




###################################################################################
#################### API ENDPOINTS =PRODUCTS ###################################
###################################################################################


@app.get("/api/version")
def version():
    return "1.0"

app.run(debug=True)