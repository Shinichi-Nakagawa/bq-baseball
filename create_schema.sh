project=$1
# Lahman Database
schema_path='schema/lahman_baseball_database/'
echo "${schema_path}*json"
for schema_file in ${schema_path}*.json; do
  # echo $schema_file
  echo "bq ${schema_file}"
  schema_name=${schema_file##*/}
  schema_name=${schema_name%%.*}
  bq mk --table \
  --schema $schema_file \
  --description "" \
  ${project}:lahman_baseball_database.${schema_name}
done
