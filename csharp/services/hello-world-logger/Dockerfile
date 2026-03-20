FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/HelloWorldLoggerService/HelloWorldLoggerService.csproj src/HelloWorldLoggerService/
RUN dotnet restore src/HelloWorldLoggerService/HelloWorldLoggerService.csproj
COPY src/HelloWorldLoggerService src/HelloWorldLoggerService
RUN dotnet publish src/HelloWorldLoggerService/HelloWorldLoggerService.csproj -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "HelloWorldLoggerService.dll"]
