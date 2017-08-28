
# Has to be set so that we can run hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-oracle

# This removes this output directory created by a previous mapreduce job
rm -rf ./mapreduce/out0

./bin/hadoop `#This is the mapreduce executable` \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=1  \
  -input ./input  \
  -output ./mapreduce/out0 \
  -mapper ./mapreduce/map0.py \
  -reducer ./mapreduce/reduce0.py 



#The following is an example of how to execute multiple mapreduce jobs in a 'pipeline' fashion
rm -rf mapreduce/out1

./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./input \
  -output ./mapreduce/out1 \
  -mapper ./mapreduce/map1.py \
  -reducer ./mapreduce/reduce1.py \
  -file ./stopwords.txt 

rm -rf mapreduce/out2

./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/out1 \
  -output ./mapreduce/out2 \
  -mapper ./mapreduce/map2.py \
  -reducer ./mapreduce/reduce2.py \
  -file ./total_document_count.txt # NOTE: This is how you make a file accessable to mapreduce jobs

rm -rf mapreduce/output

./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/out2 \
  -output ./mapreduce/output \
  -mapper ./mapreduce/map3.py \
  -reducer ./mapreduce/reduce3.py \
  -file ./total_document_count.txt # NOTE: This is how you make a file accessable to mapreduce jobs