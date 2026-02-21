output "api_invoke_url" {
  description = "Base URL for the API Gateway stage"
  value       = "https://${aws_api_gateway_rest_api.crud_api.id}.execute-api.${var.aws_region}.amazonaws.com/${var.environment}"
}
