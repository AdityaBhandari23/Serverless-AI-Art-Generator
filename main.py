import json
import boto3
import base64
import datetime
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context):
    input_prompt=event['prompt']
    print(input_prompt)

    response_bedrock = client_bedrock.invoke_model(contentType='application/json', accept='application/json',modelId='stability.stable-diffusion-xl-v1',
       body=json.dumps({"text_prompts": [{"text": input_prompt}],"cfg_scale": 10,"steps": 30,"seed": 0}))
  
    response_bedrock_byte=json.loads(response_bedrock['body'].read())
    print(response_bedrock_byte)
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    print(response_bedrock_finalimage)
    
    poster_name = 'posterName'+ datetime.datetime.today().strftime('%Y-%M-%D-%M-%S')
    
    response_s3=client_s3.put_object(
        Bucket='movieposterdesign01',
        Body=response_bedrock_finalimage,
        Key=poster_name)

    generate_presigned_url = client_s3.generate_presigned_url('get_object', Params={'Bucket':'movieposterdesign01','Key':poster_name}, ExpiresIn=3600)
    print(generate_presigned_url)
    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }
