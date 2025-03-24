"""
OpenAI Agents SDK 自定义模型接口示例
使用说明：需要先安装依赖包 pip install openai openai-agents
"""

import asyncio
from openai import AsyncOpenAI
from agents import (
    Agent, 
    Runner, 
    set_default_openai_client, 
    set_default_openai_api,
    set_tracing_disabled
)

async def main():
    # 第一步：配置自定义模型接口
    # 创建自定义OpenAI客户端，指向第三方API服务（如Deepseek）
    custom_client = AsyncOpenAI(
        base_url="https://api.deepseek.com",  # 替换为您的API服务地址
        api_key="sk-9xxxx2"  # 替换为您的API密钥
    )
    
    # 将自定义客户端设置为默认客户端
    set_default_openai_client(custom_client)
    
    # 第二步：配置API类型和跟踪选项
    # 设置使用chat_completions API（与自定义模型兼容）
    set_default_openai_api("chat_completions")
    
    # 关闭跟踪功能（可选）
    set_tracing_disabled(True)
    
    # 第三步：创建代理并执行任务
    # 创建Agent实例，使用自定义模型"deepseek-chat"
    agent = Agent(
        name="Assistant", 
        instructions="You are a helpful assistant", 
        model="deepseek-chat"  # 指定您要使用的自定义模型名称
    )

    # 运行代理，发送中文提示
    result = await Runner.run(agent, "给我讲一个笑话.")
    
    # 打印结果
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
