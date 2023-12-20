# Install the jsonlite package if you haven't already
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  install.packages("jsonlite")
}

# Load the jsonlite package
library(jsonlite)

# Read the lines of the file
lines <- readLines('clean.json')

# Initialize an empty list to store the JSON objects
data_list <- list()

# Parse each line as a JSON object and append to the list
for (i in 1:length(lines)) {
  json_line <- fromJSON(lines[i], flatten = TRUE)[["training_data"]]
  json_line$merge_data <- paste(json_line$name, json_line$duration_ms, json_line$label, sep="/")
  data_list[[i]] <- json_line$merge_data
}

# Combine the list of data frames into a single data frame
data <- do.call(rbind, data_list)
merge_data_df <- data.frame(merge_data = unlist(data_list))

# Print the imported data
# print(data)

# Save the merge_data property as a JSON file
write_json(merge_data_df, 'merge_data_output.json')

