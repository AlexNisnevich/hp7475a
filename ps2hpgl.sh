#!/usr/bin/env bash
# Requires pstoedit.
OUTPUT_FILE="out.hpgl"

rm $OUTPUT_FILE

while (( "$#" >= 2 )); do
  PS_FILE=$1
  PEN=$2
  shift 2

  HPGL_FILE="${PS_FILE%.*}.hpgl"

  pstoedit -f plot-hpgl $PS_FILE $HPGL_FILE
  cat $HPGL_FILE | sed -e "s/SP[0-9]*;/SP$PEN;/g" >> $OUTPUT_FILE
  rm $HPGL_FILE
done
