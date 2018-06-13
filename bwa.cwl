#!/usr/bin/env cwl-runner

cwlVersion: v1.0

class: CommandLineTool

hints:
  - class: DockerRequirement
    dockerPull: "mclaugsf/bwa-interview:v1"

inputs:
  - id: reference
    type: File
    inputBinding:
      position: 1
    secondaryFiles:
      - ".amb"
      - ".ann"
      - ".bwt"
      - ".fai"
      - ".pac"
      - ".sa"

  - id: fastq1
    type: File
    inputBinding:
      position: 2

  - id: fastq2
    type: File
    inputBinding:
      position: 3

arguments:
  - bwa
  - mem

outputs:
  - id: sam
    type: stdout

stdout: output.sam
