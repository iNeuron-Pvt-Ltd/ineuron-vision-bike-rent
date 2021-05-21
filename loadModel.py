from file_operations import file_methods

class loadModel:
    def predictionFromModel(self,input):
        try:
            file_loader = file_methods.File_Operation()
            bike_model = file_loader.load_model('bike_share_rf_model')
            predval = bike_model.predict(input)
            
        except Exception as ex:
            raise ex
        return predval
