module "vpc" {
  source = "./modules/vpc"
}

module "security" {
  source = "./modules/security"
  vpc_id = module.vpc.vpc_id
}

module "alb" {
  source     = "./modules/alb"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.subnet_ids
  alb_sg_id  = module.security.alb_sg_id
}

module "ecs" {
  source           = "./modules/ecs"
  subnet_ids       = module.vpc.subnet_ids
  ecs_sg_id        = module.security.ecs_sg_id
  target_group_arn = module.alb.target_group_arn
  ecr_repo_url     = module.ecr.repository_url
}

module "rds" {
  source     = "./modules/rds"
  subnet_ids = module.vpc.subnet_ids
  rds_sg_id  = module.security.rds_sg_id
}

module "ecr" {
  source = "./modules/ecr"
}
