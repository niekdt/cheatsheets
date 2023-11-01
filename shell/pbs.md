| What | How | Details |
|---|---|---|
| Start interactive shell | `qsh` | |
| Start job | `qsub $script` | |
| Run job interactively | `qsub -I` | |
| Start parameterized job | ? | |
| View my jobs | ? | | 
| CLear queued jobs | `qdel -u $user` | |
| Kill job | `qdel $id` | |
| Kill job forcefully | `qdel -f $id` | |
| Kill range of jobs | `qdel {$id_low, $id_high)` | |
| Kill array job | `qdel $id[]` | |
| Kill array job range | `qdel -t 1-10 $id[]` | |
| Kill all jobs | `qselect -u $user \| xargs qdel` | | 

# Qsub shell script options
| What | How | Details |
|---|---|---|
| Job name | `#PBS -N $name` | |
| Working directory | `#PBS -d .` | |
| Standard output log file | `#PBS -o $HOME/Logs` | |
| Error log file | `#PBS -e $HOME/ErrorLogs` | |
| Join error output with standard | `#PBS -j oe` | |
| Join standard output with error | `#PBS -j eo` | |
| Run job as array | `#PBS -t 0-10` | Each job will have a different number in the `PBS_ARRAYID` environment variable |
| Specify queue | `#PBS -q $queue` | |
| Specify server | `#PBS -q @$server` | |
| Specifiy queue at server | `#PBS -q $queue@$server` | |
| Limit computation time (wall time) | `#PBS -l walltime 60` | |
| Limit computation time (wall time) | `#PBS -l walltime 00:01:00` | |
| Limit memory usage | `#PBS -l nodes=1:ppn=4` | |
| Declare job as rerunnable | `#PBS -r y` | |
