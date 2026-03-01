## Hackathon 2026 - Traffic Crusaders 
*Hackathon Project with Marcus, Seamus, and Michael*
### Project - FlowBot 
#### Description
We set out to help make a Smart City and we decided to help tackle one of the most frustrating aspects of modern city life- traffic. With commutes spending upwards of several hours in
each direction to reach their place of work or school, small changes to flow controls can make a huge impact not just on happiness and stress reduction; but also the environment. 
Cars are at their most fuel inefficient when in the idling, stop and go traffic of the modern city. Small improvements to infrastructure can reduce emissions and decrease gas consumption. 
To address this issue, we created a foundational model called FlowBot which can be fine-tuned on traffic flow patterns of a given city to help inform light cycles and improve infrastructure. 
#### Quick Tech Facs
- Ridge Stacking Ensemble Regressor with three models:
  - LightGBMRegressor
  - XGBRegressor
  - CatBoostRegressor
- ReactJS FrontEnd with Auth0 authentication 
