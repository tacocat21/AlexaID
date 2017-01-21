

class SpeakerRecognition:
    def CreateEnrollment(Audio):

        ########### Python 2.7 #############
        import httplib, urllib, base64

        headers = {
        # Request headers
            'Content-Type': 'multipart/form-data',
            'Ocp-Apim-Subscription-Key': '{subscription key}',
        }

        params = urllib.urlencode({
            # Request parameters
            'shortAudio': '{boolean}',
        })

        try:
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/spid/v1.0/identificationProfiles/{identificationProfileId}/enroll?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
