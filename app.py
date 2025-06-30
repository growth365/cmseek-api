from flask import Flask, request, jsonify
import cmseek
import os

app = Flask(__name__)

@app.route('/detect', methods=['GET'])
def detect_cms():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400
    try:
        os.chdir('/app/CMSeeK')
        cmseek.scan(url)
        result = cmseek.Result
        return jsonify({
            'url': url,
            'cms': result.cms_name if result.detection_status else 'Unknown',
            'version': result.cms_version if result.detection_status else 'N/A'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
