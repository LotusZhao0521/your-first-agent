"""
使用langchain搭建一个最小可用Agent
"""

import os
import asyncio
from dotenv import load_dotenv

from rich.console import Console
from rich.markdown import Markdown

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient  # type: ignore

# 初始化一个llm，可以去glm注册一个，他有一款免费的大模型用
# 然后配到项目的.env中
load_dotenv()
model = os.getenv("MODEL", "")
api_key = os.getenv("API_KEY", "")
base_url = os.getenv("BASE_URL", "")

# 我使用的是豆包的大模型，和glm都会遵守openai api 规范，所以可以用langchain_openai的拓展
llm = ChatOpenAI(
    model=model,
    api_key=api_key,  # type: ignore
    base_url=base_url,
    extra_body={"thinking": {"type": "disabled"}},
    timeout=60,
)


# 初始化mcp客户端
mcp_client = MultiServerMCPClient(
    {
        "finance": {
            "command": "python",
            "args": ["mcp_servers/finance.py"],
            "transport": "stdio",
        },
    }
)


## .get_tools 是一个异步方法，并且他的输出：StructuredTool 也必须在异步环境中使用
## 所以后面全是async function
async def get_tools():
    """获取mcp客户端的工具"""
    tools = await mcp_client.get_tools()
    print("tools:", tools)
    return tools


# tools:
# [
#   StructuredTool(
#       name='get-cls-hot-news',
#       description='get the latest finance hot news from cls.cn',
#       ......
#   )
# ]


# 初始化agent，把刚才拿到的工具给agent
async def get_agent():
    """初始化agent, 绑定工具和提示词"""
    tools = await get_tools()
    system = "你是一个人工智能助手，专注于分析财经相关新闻"
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system,  # 给他一个system prompt，明确一下身份
        debug=True,  # 方便看更多信息，values表示完整的状态值，updates表示状态更新
    )  # type: ignore
    return agent


async def execute_task(task: str):
    """让绑定了工具agent去执行任务"""
    messages = {
        "messages": [
            {"role": "user", "content": task},
        ]
    }
    agent = await get_agent()
    response = await agent.ainvoke(messages)
    return response


response = asyncio.run(execute_task("帮我查一下最近的财经新闻，并且整理一下。"))

# 打印出markdown
console = Console()
md = Markdown(response["messages"][-1].content)
console.print(md)

# 这样就实现了一个能够帮你实时整理新闻的Agent，当然如果有其他数据源的话，还可以做别的事。
# 后面章节会尝试使用别的工具，让他多做一些事

# uv run 01_最小可用的Agent/01_langchain.py

# 运行于2025-11-24 8:49:00
# pylint: disable=W0105
"""
一、市场动态                                                                                                           

 1 融资余额大幅减少                                                                                                                                                                                                               
   截至11月21日，沪深两市融资余额合计减少290.6亿元至24375.59亿元，显示市场短期情绪谨慎。                                                                                                                                          
 2 港股通标的调整                                                                                                                                                                                                                 
   深交所公告，三一重工、剑桥科技自11月24日起调入港股通标的名单。                                                                                                                                                                 
 3 零跑汽车纳入恒生科技指数                                                                                                                                                                                                       
   零跑汽车（09863.HK）获纳入恒生科技指数，12月8日生效，有望吸引被动资金配置。                                                                                                                                                    
 4 A股解禁与新股                                                                                                                                                                                                                  
    • 11月24日，15家公司合计解禁109.16亿元市值限售股，南方航空（56.89亿元）、华统股份（17.42亿元）解禁规模居前。                                                                                                                  
    • 科创板新股**摩尔线程（688795）**今日申购，公司为GPU芯片解决方案提供商。                                                                                                                                                     
 5 国际市场                                                                                                                                                                                                                       
    • 韩国KOSPI指数开盘涨1.6%，日本因假期休市。                                                                                                                                                                                   
    • 外资近期减持韩国股市（本月净卖出约12万亿韩元），转而增持中国科技ETF（如“TIGER中国恒生科技”）。                                                                                                                              

二、行业与政策   
                                                                                                     
 1 锂电与储能行业展望                                                                                                                                                                                                             
   中信证券研报指出，2026年全球动力电池需求有望稳步增长，储能装机经济性提升推动国内外需求共振，产业链价格或企稳回升，固态电池产业化加速带来投资机会。                                                                             
 2 AI产业热度持续                                                                                                                                                                                                                 
    • 英伟达业绩及Q4指引超预期，谷歌发布Gemini 3模型性能显著提升，中信证券持续看好AI PCB板块。                                                                                                                                    
    • 蚂蚁集团AI产品“灵光”4天下载量破100万，分析师认为C端AI应用有望率先形成爆款。                                                                                                                                                 
 3 人形机器人加速落地                                                                                                                                                                                                             
   北京市长殷勇调研时强调，将人形机器人作为新质生产力重要抓手，推动商业化规模化应用。                                                                                                                                             
 4 资本市场政策                                                                                                                                                                                                                   
    • 16只硬科技主题基金（易方达、华泰柏瑞等）迅速获批，近期启动募集。                                                                                                                                                            
    • 国家网信办、公安部就《大型网络平台个人信息保护规定》征求意见，要求境内运营数据存储于境内。                                                                                                                                  

三、企业动态        
                                                                                                   
 1 华锋股份临时停牌                                                                                                                                                                                                               
   因筹划控制权变更事项，华锋股份（002806.SZ）今日开市起停牌。                                                                                                                                                                    
 2 京东工业通过港交所聆讯                                                                                                                                                                                                         
   京东集团旗下京东工业（拟上市代码09618.HK）通过港交所上市聆讯，有望成为工业供应链领域重要标的。                                                                                                                                 
 3 五矿资源收购延期                                                                                                                                                                                                               
   五矿资源（01208.HK）将收购英美资源巴西镍业务的截止日期延长至2026年6月30日，因欧盟审查进入第二阶段。                                                                                                                            
 4 大悦城地产退市安排                                                                                                                                                                                                             
   大悦城地产（00207.HK）申请11月27日起撤销港交所上市地位，此前已通过股份回购计划。                                                                                                                                               

四、宏观与流动性      
                                                                                                   
 1 央行公开市场操作                                                                                                                                                                                                               
   本周（11.24-11.28）央行逆回购到期规模达16760亿元，另有9000亿元MLF（11.25到期）及3000亿元买断式逆回购（11.28到期），流动性面临考验。                                                                                            
 2 成品油价格下调                                                                                                                                                                                                                 
   今日24时国内成品油调价窗口开启，机构预测或小幅下调（汽油、柴油每升约降0.05元），加满一箱油节省约2.5元。                                                                                                                        

五、其他重要事件                                                                                                         

 1 中美关系                                                                                                                                                                                                                       
   国务院副总理何立峰会见美国前国家安全事务助理哈德利，强调中美经贸应成为关系“压舱石”。                                                                                                                                           
 2 医药与科技突破                                                                                                                                                                                                                 
    • 百利天恒（688506.SH）EGFR×HER3双抗ADC药物上市申请获受理，为全球首创进入III期临床的同类药物。                                                                                                                                
    • 中科院天津工生所实现纤维素全碳素合成淀粉，转化率提升至93.3%。                                                                                                                                                               
 3 企业风险提示                                                                                                                                                                                                                   
    • 聚石化学（688669.SH）、豪尔赛（002963.SZ）因涉嫌信披违法违规被证监会立案调查。                                                                                                                                              
    • 兆易创新（603986.SH）部分董监高拟合计减持24.9万股。                                                                                                                                                                         

六、本周关注                                                                                                           

 • MSCI指数调整：11月24日收盘后实施，涉及A股及港股成分股变动。                                                                                                                                                                    
 • 重要会议：2025全球BC技术创新峰会（11.24-25）、中国锂业大会（11.24-26）、汽车供应链大会（11.24-26）召开。                                                                                                                       
 • 数据发布：德国11月IFO商业景气指数（今日）、美国11月CPI（12月18日）。                                                                                                                                                           

以上信息综合自财联社电报，供参考。如需进一步分析某领域细节，可随时告知。                                                                                                                                                          
"""
