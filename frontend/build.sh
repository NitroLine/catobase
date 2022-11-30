npm install
npm version patch
npm run build
s3cmd sync dist/ s3://${CATOBASE_WEBSITE_BUCKET}
s3cmd --recursive modify --add-header=content-type:application/javascript  s3://${CATOBASE_WEBSITE_BUCKET}/js/
s3cmd --recursive modify --add-header=content-type:text/css  s3://${CATOBASE_WEBSITE_BUCKET}/css/

