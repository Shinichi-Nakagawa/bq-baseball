project=$1
# Lahman Database
schema_path='schema/origin/'
for schema_file in ${schema_path}*.json; do
  # echo $schema_file
  schema_name=${schema_file##*/}
  schema_name=${schema_name%%.*}
  bq mk --table \
  --schema $schema_file \
  --description "" \
  ${project}:mlb.${schema_name}
done
