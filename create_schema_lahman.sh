project=$1
dataset=$2
# Lahman Database
schema_path='schema/lahman_baseball_database/'
for schema_file in ${schema_path}*.json; do
  # echo $schema_file
  schema_name=${schema_file##*/}
  schema_name=${schema_name%%.*}
  bq mk --table \
  --schema $schema_file \
  --description "" \
  ${project}:${dataset}.${schema_name}
done
