library(dplyr) #for random samples
datasource <- "datasource/bc.csv"

main <- function() {
        dataset <- read.csv(datasource)
        str(dataset)
        
        set.seed(42) #important if replication is desired
        quantity <- 5
        random_samples <- sample_n(dataset, quantity)
        
        length(random_samples)
        
        # if (optionalArgument) {
        #         42
        # }
}