function translate(value, min1, max1, min2, max2) {
  return percentToRange(min2, max2, rangeToPercent(min1, max1, value));
}

function rangeToPercent(min, max, value) {
  return (value - min) / (max - min);
}

function percentToRange(min, max, percent) {
  return min + percent * (max - min);
}
