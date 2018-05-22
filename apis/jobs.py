from flask_restplus import Namespace, Resource, fields,reqparse

api = Namespace('jobs', description='Jobs related operations.')

"""
cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)
"""

uploadJobsRequestParams=reqparse.RequestParser()
uploadJobsRequestParams.add_argument("request_ref",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("priority",type=str,required=True,help="priority of the job.")
uploadJobsRequestParams.add_argument("start_after",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("due_ts",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("initial_estimate_hours",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("job_type_desc",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("latitude",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("longitude",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("dependency",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("skills",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("core_area",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("location_code",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("job_source",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("job_type",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("target_attended_ts",type=str,required=True,help="Id of the job.")
uploadJobsRequestParams.add_argument("target_attended_duration",type=str,required=True,help="Id of the job.")

@api.route("/upload_jobs")
class UploadJobs(Resource):
    @api.doc("Upload jobs")
    @api.expect()