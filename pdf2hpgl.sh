#!/usr/bin/env bash
# Requires pdf2ps and pstoedit.
OUTPUT_FILE="out.hpgl"

rm $OUTPUT_FILE

while (( "$#" >= 2 )); do
  PNG_FILE=$1
  PEN=$2
  shift 2

  PS_FILE="${PNG_FILE%.*}.ps"
  HPGL_FILE="${PNG_FILE%.*}.hpgl"

  pdf2ps $PNG_FILE $PS_FILE
  pstoedit -f plot-hpgl $PS_FILE $HPGL_FILE
  cat $HPGL_FILE | sed -e "s/SP[0-9]*;/SP$PEN;/g" >> $OUTPUT_FILE
done
