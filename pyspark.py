from pyspark.sql.functions import col


def get_pairs(product_df, categories_df):
    joined = product_df.join(categories_df, products_df["product_id"] == categories_df["product_id"], "left")
    result = joined.select(products_df["product_name"], categories_df["category_name"], col("categories.product_id").isNull().alias("no_category"))
    products_with_no_category = result.filter(col("no_category"))
    
    return result_df, products_no_category