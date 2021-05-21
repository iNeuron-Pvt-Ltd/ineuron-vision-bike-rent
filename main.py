from flask import Flask, request, redirect, render_template, Response
from flask_cors import CORS, cross_origin
from form_data.user_input import user_input
from loadModel import loadModel

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def predict():
    try:
        if request.form is not None:
            input_values = request.form
            user_ip = user_input(input_values)

            if user_ip.df.empty:
                return render_template('index.html')
            else:
                inpv = user_ip.get_user_input(user_ip.df)
                bike_model = loadModel()
                # bike_model = pikl.load(open(r'model\bike_share_rf_model.P', 'rb'))
                predval = bike_model.predictionFromModel(inpv)
                
                return render_template('index.html', result=predval[0], predict=1)
        else:
            return redirect('/')
    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG_MODE)
    app.run(debug=True)
