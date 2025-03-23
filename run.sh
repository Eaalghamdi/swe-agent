# sweagent run-batch \
#     --instances.type huggingface \
#     --agent.model.name claude-3-5-sonnet-20241022 \
#     --agent.model.per_instance_cost_limit 2.00 \
#     --config config/default.yaml \
#     --instances.dataset_name "eaalghamdi/swe_bench_verfied_PI" \
#     --instances.split "test" \
#     --instances.slice :3 \
#     --instances.shuffle False \


# sweagent run-batch \
#     --config config/default.yaml \
#     --agent.model.name claude-3-5-sonnet-20241022 \
#     --agent.model.per_instance_cost_limit 2.00 \
#     --instances.type swe_bench \
#     --instances.subset light \
#     --instances.split dev  \
#     --instances.slice :1 \
#     --instances.shuffle False\
#     --instances.evaluate True\

# single issue in a github repo
sweagent run \
  --config config/secure.yaml \
  --config config/secure_issue.yaml \
  --agent.model.name=claude-3-5-sonnet-20241022 \
  --agent.model.per_instance_cost_limit=2.00 \
#   --env.repo.github_url=https://github.com/Eaalghamdi/test-repo \
#   --problem_statement.path = secure_issue.md \

